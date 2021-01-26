#!python39
##
# デイリーイベントを各2回(1日に参加できる上限)挑戦する
# 事前準備
# - バトルがautoモードになっていること
# - バトルが早送りになっていること
# - 戦闘力が40,000以上になっていること
##
from lib.adb import Adb
from lib import last_bullet

from time import sleep

# デイリーイベント画面を開く
def go_to_daily_event(adb):
	last_bullet.go_to_home(adb)
	sleep(3)
	last_bullet.go_to_battle(adb)
	sleep(3)
	last_bullet.go_to_event_battle(adb)
	sleep(3)
	last_bullet.select_daily_event(adb)
	sleep(3)

# バトルを2回実行する
def battle2(adb):
	sleep(3)
	last_bullet.select_unit(adb) # ユニット選択
	sleep(30)## 暫定的
	last_bullet.sortie(adb) # 出撃
	sleep(120)
	last_bullet.replay(adb) # 再戦
	sleep(120)
	last_bullet.stage_clear_ok(adb) # OK
	sleep(3)

def collect_coin(adb):
	go_to_daily_event(adb)
	sleep(3)
	adb.tap(935, 235) # コイン収集任務
	sleep(3)
	adb.tap(1500, 662) # ステージ03
	sleep(3)
	battle2(adb)

def strengthen_memoria(adb):
	go_to_daily_event(adb)
	sleep(3)
	adb.tap(1651, 235) # メモリ強化任務
	sleep(3)
	adb.tap(1500, 662) # ステージ03
	sleep(3)
	battle2(adb)

def evolve_memoria(adb):
	go_to_daily_event(adb)
	sleep(3)
	adb.tap(935, 552) # メモリ進化任務
	sleep(3)
	adb.tap(1500, 662) # ステージ03
	sleep(3)
	battle2(adb)

def strengthen_charm(adb):
	go_to_daily_event(adb)
	sleep(3)
	adb.tap(1622, 564) # CHARM強化任務
	sleep(3)
	adb.tap(1500, 662) # ステージ03
	sleep(3)
	battle2(adb)

def evolve_charm(adb):
	go_to_daily_event(adb)
	sleep(3)
	adb.tap(892, 898) # CHARM進化任務
	sleep(3)
	adb.tap(1500, 662) # ステージ03
	sleep(3)
	battle2(adb)

def evolve_charm_power(adb):
	go_to_daily_event(adb)
	sleep(3)
	adb.tap(1673, 892) # CHARM出力強化任務
	sleep(3)
	adb.tap(1500, 662) # ステージ03
	sleep(3)
	battle2(adb)

# メインシナリオ
def scenario(adb):
	collect_coin(adb)
	strengthen_memoria(adb)
	# evolve_memoria(adb)## 色ごとに進化素材が違うので調整が必要
	strengthen_charm(adb)
	evolve_charm(adb)
	evolve_charm_power(adb)

	# battle2(adb)
if __name__ == '__main__':
	with Adb('5b09ee92') as adb:
		scenario(adb)
