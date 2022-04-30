from libgravatar import Gravatar

def get_user_image(email) -> str:
    g = Gravatar(email)
    image = g.get_image(default='retro')
    return image

def util_calculate_age(dob, dod) -> int:
    return dod.year - dob.year - ((dod.month, dod.day) < (dob.month, dob.day))