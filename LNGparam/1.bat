cls
@rem Python 3.7.3

@rem Испания/Chrome 77.0.3865/ passed
@rem 1. Тест в репозитории можно запустить командой pytest --language=es, тест успешно проходит.
pytest -v -s --language=es test_items.py

@rem Франция/Firefox 68.02/ passed
@rem pytest -v -s --language=fr --browser_name=firefox test_items.py
pytest -v -s --language=fr test_items.py

@rem Россия/Chrome 77.0.3865/ passed
pytest -v -s --language=ru test_items.py

@rem ЗападныйЗанЗибар/Chrome 77.0.3865/ failed - language NO support
pytest -v -s --language=zzz test_items.py