class Creature:
    def __init__(self, name, attack, defence):
        self.name = name
        self.attack = attack
        self.defence = defence

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defence})'


class CreatorModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatorModifier):
    def handle(self):
        print(f'Doubling {self.creature.name}\'s attack')
        self.creature.attack *= 2
        super().handle()


class NoBonusesModifier(CreatorModifier):
    def handle(self):
        print('No bonuses for you')


class IncreaseDefenseModifier(CreatorModifier):

    def handle(self):
        if self.creature.attack <= 2:
            print(f'Increasing {self.creature.name} defense')
            self.creature.defence += 1
        super().handle()


if __name__ == '__main__':
    goblin = Creature('Goblin', 1, 1)
    print(goblin)

    root = CreatorModifier(goblin)

    root.add_modifier(NoBonusesModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))

    root.handle()
    print(goblin)
