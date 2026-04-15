from pydantic import BaseModel

class PostStudent(BaseModel):
    first_name: str
    last_name: str | None = None
    short_name: str | None = None
    birthdate: str | None = None
    languages: list | None = None
    allergies: list | None = None
    appetite: str | None = None
    food_likes: list | None = None
    food_dislikes: list | None = None
    food_restrictions: list | None = None
    self_feeding: bool | None = True
    feeding_notes: str | None = None
    breakfast_time: str | None = None
    lunch_time: str | None = None
    snack_time: str | None = None
    supper_time: str | None = None
    in_diapers: bool | None = True
    toilet_training_status: str | None = None
    toilet_training_notes: str | None = None
    self_dressing: bool | None = True
    dressing_notes: str | None = None
    naps: bool | None = True
    nap_notes: str | None = None
    separation: bool | None = True
    separation_notes: str | None = None
    shyness: bool | None = True
    shyness_notes: str | None = None
    fears: list | None = None
    fears_notes: str | None = None
    shows_affection: str | None = None
    shows_fear: str | None = None
    shows_anger: str | None = None
    shows_frustration: str | None = None
    shows_excitement: str | None = None
    favored_item_notes: str | None = None
    play_experience_notes: str | None = None
    imaginary_play_notes: str | None = None
    liked_activities_notes: str | None = None
    disliked_activities_notes: str | None = None
    discipline_notes: str | None = None
    development_encouraged: str | None = None
    development_discouraged: str | None = None
    notes: str | None = None
    image: str | None = None