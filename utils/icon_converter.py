def convert_to_icon(icon, moon_phase=0):
    if "clear-day" == icon:
        return 'resources\\weather_images\\clear-day.png'
    elif "rain" == icon:
        return 'resources\\weather_images\\rain.png'
    elif "snow" == icon:
        return 'resources\\weather_images\\snow.png'
    elif "sleet" == icon:
        return 'resources\\weather_images\\sleet.png'
    elif "wind" == icon:
        return 'resources\\weather_images\\wind.png'
    elif "fog" == icon:
        return 'resources\\weather_images\\fog.png'
    elif "cloudy" == icon:
        return 'resources\\weather_images\\cloudy.png'
    elif "partly-cloudy-day" == icon:
        return 'resources\\weather_images\\partly-cloudy-day.png'
    elif "clear-night" == icon:
        if moon_phase <= 0.12:
            return 'resources\\weather_images\\clear-night-0.png'
        elif moon_phase > 0.12 and moon_phase < 0.37:
            return 'resources\\weather_images\\clear-night-25.png'
        elif moon_phase > 0.37 and moon_phase < 0.62:
            return 'resources\\weather_images\\clear-night-50.png'
        elif moon_phase > 0.62 and moon_phase < 0.78:
            return 'resources\\weather_images\\clear-night-75.png'
        elif moon_phase > 0.78:
            return 'resources\\weather_images\\clear-night-100.png'
    elif "partly-cloudy-night" == icon:
        if moon_phase <= 0.12:
            return 'resources\\weather_images\\partly-cloudy-night-0.png'
        elif moon_phase > 0.12 and moon_phase < 0.37:
            return 'resources\\weather_images\\partly-cloudy-night-25.png'
        elif moon_phase > 0.37 and moon_phase < 0.62:
            return 'resources\\weather_images\\partly-cloudy-night-50.png'
        elif moon_phase > 0.62 and moon_phase < 0.78:
            return 'resources\\weather_images\\partly-cloudy-night-75.png'
        elif moon_phase > 0.78:
            return 'resources\\weather_images\\partly-cloudy-night-100.png'
    else:
        return 'resources\\weather_images\\na.png'
