def controller(positions, references, time_step):

    Kp = 0.15
    Kd = 0.6

    ref = references[time_step]
    pos = positions[2, time_step]

    #on first step, use a preset value for prev_error since there is no previous step to reference
    if time_step == 0:
        

        #preset previous error to -1 for first step (no previous step)
        prev_error = -1
        #find current error
        error = ref - pos
        
    #for all other steps, calculate error and previous error
    else:
        prev_ref = references[time_step - 1]
        prev_pos = positions[time_step - 1]
        prev_error = prev_ref - prev_pos
        error = ref - pos


    #Error at this time step
    error = ref - pos
    prev_error = prev_ref - prev_pos

    #Calculate output control signal using PD control law
    output = Kp * error + Kd * (error - prev_error)
    return output