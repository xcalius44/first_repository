class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.dark_mode = True
        self.bg_color = (0, 0, 0) if self.dark_mode else (230, 230, 230)

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0) if self.dark_mode else (60, 60, 60)
        self.bulets_allowed = 3

        self.fleet_drop_speed = 10

        self.star_limit = 100
        self.star_speed = 0.09
        self.star_start_color = 200
        self.star_color_limit = 256
        self.star_color_step = 0.15
        self.star_radius = 3

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialyze_dynamic_settings()

    def initialyze_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
