import os, json, pygame

def create_save():

    # logic, save file, the control string matches with a profile, the chosen profile one or zero
    # a string matches a string matches a dictionary
    new_save = {
            'controls' :{
            '0' :{'Left': pygame.K_a, 'Right': pygame.K_d, 'Up': pygame.K_w,
                'Down': pygame.K_s, 'Start': pygame.K_RETURN, 'Action1': pygame.K_SPACE},
            '1' :{'Left': pygame.K_a, 'Right': pygame.K_d, 'Up': pygame.K_w, 'Down': pygame.K_s,
                'Start': pygame.K_RETURN, 'Action1': pygame.K_SPACE}
            },
            'current_profile': 0
            }

    return new_save

def load_save():

    try:
        # attempt to retreive save from disk
        save = load_existing_save('../game_data/save.json')
    except:
        # No save file, create one
        save = create_save()
        write_save(save)

    return save

def load_existing_save(savefile):
    with open(os.path.join(savefile), 'r+') as file:
        controls = json.load(file)
    return controls

def write_save(data):
    print(os.getcwd())
    with open(os.path.join(os.getcwd(), '../game_data/save.json'), 'w') as file:
            json.dump(data, file)

def reset_keys(actions):
    for action in actions:
        actions[action] = False
