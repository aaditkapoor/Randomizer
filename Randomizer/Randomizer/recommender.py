import numpy as np
import os
from .models import UserDataModel

all_users = UserDataModel.objects.all()

def recommend(user_items):
    pass