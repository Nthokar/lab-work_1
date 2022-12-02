# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #5 выполнил(а):
- Жирнов Владимир Андреевич
- РИ-210947
Отметка о выполнении заданий (заполняется студентом):

| Задание | Выполнение | Баллы |
| ------ | ------ | ------ |
| Задание 1 | * | 60 |
| Задание 2 | * | 100 |

знак "*" - задание выполнено; знак "#" - задание не выполнено;

Работу проверили:
- к.т.н., доцент Денисов Д.В.
- к.э.н., доцент Панов М.А.
- ст. преп., Фадеев В.О.

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Структура отчета

- Данные о работе: название работы, фио, группа, выполненные задания.
- Цель работы.
- Задание 1.
- Код реализации выполнения задания. Визуализация результатов выполнения (если применимо).
- Задание 2.
- Код реализации выполнения задания. Визуализация результатов выполнения (если применимо).
- Выводы.
- ✨Magic ✨

## Цель работы
Ознакомиться с интеграцией экономической системы в проект Unity и обучением ML-Agent

## Задание 1
### Измените параметры файла .yaml-агента и определить какие параметры и как влияют на обучение модели.
```
behaviors:
  Economic:
    trainer_type: ppo
    hyperparameters:
      batch_size: 1024
      buffer_size: 10240
      learning_rate: 3.0e-4
      learning_rate_schedule: linear
      beta: 1.0e-4 # <= 1.0e-2(default)
      epsilon: 0.5 # <= 0.2(default)
      lambd: 0.95
      num_epoch: 6 # <= 3(default)    
    network_settings:
      normalize: false
      hidden_units: 128
      num_layers: 2
    reward_signals:
      extrinsic:
        gamma: 0.99
        strength: 0.8 # <= 1.0(default)
    checkpoint_interval: 500000
    max_steps: 750000
    time_horizon: 64
    summary_freq: 5000
    self_play:
      save_steps: 20000
      team_change: 100000
      swap_steps: 10000
      play_against_latest_model_ratio: 0.5
      window: 10
```
- beta - Сила регуляризации энтропии. beta-значение должно быть скорректировано таким образом, чтобы энтропия (можно посмотреть в TensorBoard) медленно уменьшалась вместе с увеличением вознаграждения.

- epsilon - Соответствует допустимому порогу расхождения между старой и новой политиками обучения при обновлении с градиентным спуском. Установка этого значения небольшим приведет к более стабильным обновлениям, но также замедлит процесс обучения.

- num_epoch - Количество проходов через буфер опыта при выполнении оптимизации градиентного спуска. Уменьшение этого параметра обеспечит более стабильные обновления за счет более медленного обучения.
- strength - Коэффициент, на который умножается вознаграждение, данное средой. Типичные диапазоны будут варьироваться в зависимости от сигнала вознаграждения.
- 
## Задание 2
### Опишите результаты, выведенные в TensorBoard.

start

![image](https://github.com/Nthokar/lab-work_1/blob/lab_work_5/screenshots/startEnvironment.jpg)

![image](https://github.com/Nthokar/lab-work_1/blob/lab_work_5/screenshots/startLosses.jpg)

![image](https://github.com/Nthokar/lab-work_1/blob/lab_work_5/screenshots/startPolicy.jpg)

with changes in economic.yaml

![image](https://github.com/Nthokar/lab-work_1/blob/lab_work_5/screenshots/ExampleEnviroment.jpg)

![image](https://github.com/Nthokar/lab-work_1/blob/lab_work_5/screenshots/ExampleLosses.jpg)

![image](https://github.com/Nthokar/lab-work_1/blob/lab_work_5/screenshots/ExamplePolicy.jpg)

Cumulative Rewards - Накопленное вознаграждение, должно постоянно увеличиваться пока не дойдет до стабильного значения.

Episode Length - Длительность эпизода, со временема должен уменьшаться, т.к при правильном обучении агент должен решать задачу с каждой итерацией быстрее.

Policy Loss — это потеря предсказания наилучшего хода. Агент пытается предсказать, каким будет наилучшее действие в текущей ситуации. Это политика. Потери политики измеряются тем, насколько это было неправильно.

Value loss- коэффициент, который также должен уменьшаться со временем, поскольку модель становится более точной с каждым новым эпизодом.

После изменения настроек обучения можно заметить, что графики Cumulative Reward, Value Loss, Beta изменились. Cumulative Reward растет на протяжении всего времени обучения. Policy Loss примерно равно нулю на протяжении всего обучения. Value Loss стремится к нулю, что может быть показателем успешного обучения.

## Выводы
В данной работе я внедрили экономическую систему и обучение ML-агента в преокт Unity и познакомились с TensorBoard.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Powered by

**BigDigital Team: Denisov | Fadeev | Panov**
