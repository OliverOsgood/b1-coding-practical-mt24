def controller(obs, ref):
    Kp = 0
    Ki = 0
    Kd = 0
    error = ref - obs

    output = Kp* error + Ki*error + Kd*error
    return output