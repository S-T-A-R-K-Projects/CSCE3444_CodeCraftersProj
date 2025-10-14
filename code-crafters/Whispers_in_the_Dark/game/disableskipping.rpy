init python:
    # 1) Strip out all skip/toggle/fast-skip keys
    config.keymap['skip'] = []
    config.keymap['toggle_skip'] = []
    config.keymap['fast_skip'] = []

    # 2) Remove Enter/Space/Numpad-Enter and left-click from advancing (“dismiss”)
    for k in ('K_RETURN', 'K_SPACE', 'K_KP_ENTER'):
        if k in config.keymap['dismiss']:
            config.keymap['dismiss'].remove(k)

    # 3) Remove PageUp/scroll-up from rollback
    for k in ('any_K_PAGEUP', 'any_KP_PAGEUP', 'mousedown_4'):
        if k in config.keymap['rollback']:
            config.keymap['rollback'].remove(k)

    # 4) Remove PageDown/scroll-down from rollforward
    for k in ('any_K_PAGEDOWN', 'any_KP_PAGEDOWN', 'mousedown_5'):
        if k in config.keymap['rollforward']:
            config.keymap['rollforward'].remove(k)

    # 5) (Optional) Disable mouse-wheel scrolling in viewports
    config.keymap['viewport_wheelup'] = []
    config.keymap['viewport_wheeldown'] = []

    # 6) Apply all changes immediately
    renpy.clear_keymap_cache()
