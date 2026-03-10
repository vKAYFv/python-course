import sys, os

collect_ignore = []

# Этот код выполняется при загрузке conftest — ДО импорта тест-модуля
_here = os.path.dirname(os.path.abspath(__file__))

# Сбрасываем кэш задач из других модулей
for key in list(sys.modules.keys()):
    if key in ('tasks', 'solution', 'theory'):
        del sys.modules[key]

# Наша папка — первая в path
if _here in sys.path:
    sys.path.remove(_here)
sys.path.insert(0, _here)