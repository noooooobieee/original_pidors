from datetime import datetime, timedelta

class Pokemon:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.last_feed_time = datetime.now()

    def feed(self, feed_interval=20, hp_increase=10):
        current_time = datetime.now()
        delta_time = timedelta(minutes=feed_interval)
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона {self.name} увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона {self.name}: {self.last_feed_time + delta_time}"


class Wizard(Pokemon):
    def feed(self, feed_interval=10, hp_increase=10):
        return super().feed(feed_interval, hp_increase)


class Fighter(Pokemon):
    def feed(self, feed_interval=20, hp_increase=20):
        return super().feed(feed_interval, hp_increase)


# Testing the code
pikachu = Pokemon("Pikachu", 100)
print(pikachu.feed())  # Should return "Здоровье покемона Pikachu увеличено. Текущее здоровье: 110"

wizard = Wizard("Wizard", 80)
print(wizard.feed())  # Should return "Здоровье покемона Wizard увеличено. Текущее здоровье: 90"

fighter = Fighter("Fighter", 120)
print(fighter.feed())  # Should return "Здоровье покемона Fighter увеличено. Текущее здоровье: 140"
