import random

@service
def candle_light(**params):
    entity_id = params.get('entity_id')
    if entity_id is None:
        log.error(f'candle_light: entity_id required. saw {params}')
        return

    if not entity_id.startswith('light.'):
        log.error(f'candle_light {entity_id}: entity_id must be a light')
        return

    task.unique(f'candle_light_{entity_id}')

    state = params.get('state')
    if state != 'on':
        log.info(f'candle_light {entity_id}: stopping')
        return

    log.info(f'candle_light {entity_id}: starting')

    brightness = params.get('brightness', 12)
    brightness_min = max(brightness - 10, 0)
    brightness_max = min(brightness + 10, 255)

    color_temp = params.get('color_temp', 450)
    color_temp_min = round(color_temp * 0.9)
    color_temp_max = round(color_temp * 1.1)

    delay = params.get('delay', 500)
    delay_min = round(delay * 0.5)
    delay_max = round(delay * 1.5)

    log.info(f'candle_light {entity_id}: brightness {brightness_min}-{brightness_max}, color_temp {color_temp_min}-{color_temp_max}, delay {delay_min}-{delay_max}')

    while True:
        color_temp = random.randint(color_temp_min, color_temp_max)
        brightness = random.randint(brightness_min, brightness_max)
        delay = (random.randint(delay_min, delay_max)) / 1000
        light.turn_on(
            entity_id=entity_id,
            brightness=brightness,
            color_temp=color_temp,
            transition=delay
        )

        task.sleep(delay)
