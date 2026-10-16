def controller(positions, references, time_step):

    Kp = 0.15
    Kd = 0.6

    ref = references[time_step]

    pos = positions[time_step, 1]

    if time_step == 0:
        prev_error = -1
        error = ref - pos
    else:
        prev_ref = references[time_step - 1]
        prev_pos = positions[time_step - 1, 1]
        prev_error = prev_ref - prev_pos
        error = ref - pos


    #Calculate output control signal using PD control law
    output = Kp * error + Kd * (error - prev_error)
    return output