class QueryBuilder:
    def __init__(self):
        self.query = Query()

    def build(self):
        return self.query
    
    def plays_in(self, team):
        self.query.plays_in(team)
        return self
    
    def has_at_least(self, value, attr):
        self.query.has_at_least(value, attr)
        return self

    def has_fewer_than(self, value, attr):
        self.query.has_fewer_than(value, attr)
        return self
    
    def one_of(self, *queries):
        self.query.one_of(*queries)
        return self
    
class Query:
    def __init__(self):
        self._matchers = []

    def all(self):
        self._matchers.append(All())
        return self
    
    def plays_in(self, team):
        self._matchers.append(lambda player: player.team == team)
        return self
    
    def has_at_least(self, value, attr):
        self._matchers.append(lambda player: getattr(player, attr) >= value)
        return self

    def has_fewer_than(self, value, attr):
        self._matchers.append(lambda player: getattr(player, attr) < value)
        return self
    
    def one_of(self, *queries):
        self._matchers.append(lambda player: any(query.test(player) for query in queries))
        return self
    
    def test(self, player):
        if not self._matchers:
            return True
        for matcher in self._matchers:
            if not matcher(player):
                return False
        return True

class All:
    def __init__(self):
        pass

    def test(self, player):
        return True
    

'''
class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)
    
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
'''