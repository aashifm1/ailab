class CandidateElimination:
    def _init_(self, attributes):
        self.G = []
        self.S = []
        self.attributes = attributes

    def initialize(self):
        self.S = [self.get_most_specific_hypothesis()]
        self.G = [self.get_most_general_hypothesis()]

    def get_most_specific_hypothesis(self):
        return ['?' for _ in self.attributes]

    def get_most_general_hypothesis(self):
        return ['0' for _ in self.attributes]

    def refine_hypotheses(self, instance, target):
        if target == '1':
            self.S = [self.refine_specific_hypothesis(s, instance) for s in self.S]
            self.G = [g for g in self.G if self.is_more_general(g, instance)]
        else:
            self.G = [self.refine_general_hypothesis(g, instance) for g in self.G]
            self.S = [s for s in self.S if not self.is_more_specific(s, instance)]

    def refine_specific_hypothesis(self, s, instance):
        return [s[i] if s[i] == instance[i] or s[i] == '?' else '?' for i in range(len(s))]

    def refine_general_hypothesis(self, g, instance):
        return [g[i] if g[i] == '0' or g[i] == instance[i] else '?' for i in range(len(g))]

    def is_more_general(self, g, instance):
        return all(g[i] == '0' or g[i] == instance[i] for i in range(len(g)))

    def is_more_specific(self, s, instance):
        return any(s[i] != '?' and s[i] != instance[i] for i in range(len(s)))

    def fit(self, data):
        self.initialize()
        for instance in data:
            features = instance[:-1]
            target = instance[-1]
            self.refine_hypotheses(features, target)

    def get_version_space(self):
        return self.S, self.G

if __name__ == "_main_":
    attributes = ['color', 'size', 'shape']
    data = [
        ['green', 'small', 'circle', '1'],
        ['yellow', 'large', 'circle', '1'],
        ['green', 'large', 'square', '0'],
        ['yellow', 'small', 'square', '0'],
        ['green', 'small', 'triangle', '1'],
        ['yellow', 'large', 'triangle', '1'],
    ]

    ce = CandidateElimination(attributes)
    ce.fit(data)
    specific_hypotheses, general_hypotheses = ce.get_version_space()

    print("Specific Hypotheses:", specific_hypotheses)
    print("General Hypotheses:", general_hypotheses)