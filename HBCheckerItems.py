# HBChecker by Epicpkmn11
# https://github.com/Epicpkmn11/DSi-HB-Checker/
# The first line is used for determining if that set is present, all others are checked for after

fileSets = {
	'1 HiyaCFW': [
		'bootcode.dsi \nThis is used to determine what to check',
		'bootcode.dsi \nFrom the downloaded "HiyaCFW/for SDNAND SD card"',
		'hiya/bootloader.nds \nFrom the downloaded "HiyaCFW/for PC/Modified Files" after running HiyaCFW Helper',
		'shared1/TWLCFG0.dat \nFrom your NAND backup',
		'shared1/TWLCFG1.dat \nFrom your NAND backup',
		'shared2/0000 \nFrom your NAND backup',
		'shared2/launcher/wrap.bin \nFrom your NAND backup',
		'sys/cert.sys \nFrom your NAND backup',
		'sys/dev.kp \nFrom your NAND backup',
		'sys/HWID.sgn \nFrom your NAND backup',
		'sys/HWINFO_N.dat \nFrom your NAND backup',
		'sys/HWINFO_S.dat \nFrom your NAND backup',
		'sys/TWLFontTable.dat \nFrom your NAND backup'
	],
	'2 HiyaCFW USA': [
		'title/00030017/484e4145/content/00000002.app \nThis is used to determine what to check',
		'title/00030017/484e4145/content/00000002.app \nFrom the downloaded "HiyaCFW/for PC/Modified Files" after running HiyaCFW Helper',
		'title/00030017/484e4145/content/title.tmd \nFrom the downloaded "HiyaCFW/for SDNAND SD card"'
	],
	'3 HiyaCFW JPN': [
		'title/00030017/484e414a/content/00000002.app \nThis is used to determine what to check',
		'title/00030017/484e414a/content/00000002.app \nFrom the downloaded "HiyaCFW/for PC/Modified Files" after running HiyaCFW Helper',
		'title/00030017/484e414a/content/title.tmd \nFrom the downloaded "HiyaCFW/for SDNAND SD card"'
	],
	'4 HiyaCFW EUR': [
		'title/00030017/484e4150/content/00000002.app \nThis is used to determine what to check',
		'title/00030017/484e4150/content/00000002.app \nFrom the downloaded "HiyaCFW/for PC/Modified Files" after running HiyaCFW Helper',
		'title/00030017/484e4150/content/title.tmd \nFrom the downloaded "HiyaCFW/for SDNAND SD card"'
	],
	'5 HiyaCFW AUS': [
		'title/00030017/484e4155/content/00000002.app \nThis is used to determine what to check',
		'title/00030017/484e4155/content/00000002.app \nFrom the downloaded "HiyaCFW/for PC/Modified Files" after running HiyaCFW Helper',
		'title/00030017/484e4155/content/title.tmd \nFrom the downloaded "HiyaCFW/for SDNAND SD card"'
		],
	'6 TWLMenu': [
		'_nds/TWiLightMenu/main.srldr \nThis is used to determine what to check',
		'BOOT.NDS \nFrom the downloaded "TWiLightMenu"',
		'_nds/GBARunner2_fc.nds \nFrom the downloaded "TWiLightMenu"',
		'_nds/GBARunner2.nds \nFrom the downloaded "TWiLightMenu"',
		'_nds/nds-bootstrap-hb-nightly.nds \nFrom the downloaded "TWiLightMenu"',
		'_nds/nds-bootstrap-hb-release.nds \nFrom the downloaded "TWiLightMenu"',
		'_nds/nds-bootstrap-nightly.nds \nFrom the downloaded "TWiLightMenu"',
		'_nds/nds-bootstrap-release.nds \nFrom the downloaded "TWiLightMenu"',
		'_nds/nds-bootstrap.ini \nFrom the downloaded "TWiLightMenu"',
		'_nds/TWiLightMenu/dsimenu.srldr \nFrom the downloaded "TWiLightMenu"',
		'_nds/TWiLightMenu/gbaswitch.srldr \nFrom the downloaded "TWiLightMenu"',
		'_nds/TWiLightMenu/main.srldr \nFrom the downloaded "TWiLightMenu"',
		'_nds/TWiLightMenu/nightly-bootstrap.ver \nFrom the downloaded "TWiLightMenu"',
		'_nds/TWiLightMenu/r4menu.srldr \nFrom the downloaded "TWiLightMenu"',
		'_nds/TWiLightMenu/release-bootstrap.ver \nFrom the downloaded "TWiLightMenu"',
		'_nds/TWiLightMenu/slot1launch.srldr \nFrom the downloaded "TWiLightMenu"',
		'_nds/TWiLightMenu/emulators/gameyob.nds \nFrom the downloaded "TWiLightMenu"',
		'_nds/TWiLightMenu/emulators/nesds.nds \nFrom the downloaded "TWiLightMenu"',
		'_nds/TWiLightMenu/emulators/nestwl.nds \nFrom the downloaded "TWiLightMenu"',
		'hiya/autoboot.bin \nFrom the downloaded "TWiLightMenu/Autoboot for HiyaCFW"',
		'title/00030015/534c524e/content/00000000.app \nFrom the downloaded "TWiLightMenu/CFW - SDNAND root"',
		'title/00030015/534c524e/content/title.tmd \nFrom the downloaded "TWiLightMenu/CFW - SDNAND root"',
		'title/00030015/53524c41/content/00000000.app \nFrom the downloaded "TWiLightMenu/CFW - SDNAND root"',
		'title/00030015/53524c41/content/title.tmd \nFrom the downloaded "TWiLightMenu/CFW - SDNAND root"'
	],
	'7 DSiMenuPP 6.2.0': [
		'_nds/dsimenuplusplus/release-bootstrap.ver \nThis is used to determine what to check',
		'BOOT.NDS \nFrom the downloaded "DSiMenuPP"',
		'_nds/GBARunner2_fc.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/GBARunner2.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap-hb-nightly.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap-hb-release.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap-nightly.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap-release.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap.ini \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/dsimenu.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/gbaswitch.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/main.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/nightly-bootstrap.ver \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/r4menu.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/release-bootstrap.ver \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/slot1launch.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/emulators/gameyob.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/emulators/nesds.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/emulators/nestwl.nds \nFrom the downloaded "DSiMenuPP"',
		'hiya/autoboot.bin \nFrom the downloaded "DSiMenuPP/Autoboot for HiyaCFW"',
		'title/00030015/534c524e/content/00000000.app \nFrom the downloaded "DSiMenuPP/CFW - SDNAND root"',
		'title/00030015/534c524e/content/title.tmd \nFrom the downloaded "DSiMenuPP/CFW - SDNAND root"',
		'title/00030015/53524c41/content/00000000.app \nFrom the downloaded "DSiMenuPP/CFW - SDNAND root"',
		'title/00030015/53524c41/content/title.tmd \nFrom the downloaded "DSiMenuPP/CFW - SDNAND root"'
	],
	'8 DSiMenuPP 6.0.0': [
		'_nds/dsimenuplusplus/release-bootstrap \nThis is used to determine what to check',
		'BOOT.NDS \nFrom the downloaded "DSiMenuPP"',
		'_nds/GBARunner2_fc.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/GBARunner2.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap-hb-nightly.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap-hb-release.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap-nightly.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap-release.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap.ini \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/dsimenu.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/gbaswitch.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/main.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/nightly-bootstrap \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/r4menu.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/release-bootstrap \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/slot1launch.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/emulators/gameyob.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/emulators/nesds.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/emulators/nestwl.nds \nFrom the downloaded "DSiMenuPP"',
		'hiya/autoboot.bin \nFrom the downloaded "DSiMenuPP/Autoboot for HiyaCFW"',
		'title/00030015/534c524e/content/00000000.app \nFrom the downloaded "DSiMenuPP/CFW - SDNAND root"',
		'title/00030015/534c524e/content/title.tmd \nFrom the downloaded "DSiMenuPP/CFW - SDNAND root"',
		'title/00030015/53524c41/content/00000000.app \nFrom the downloaded "DSiMenuPP/CFW - SDNAND root"',
		'title/00030015/53524c41/content/title.tmd \nFrom the downloaded "DSiMenuPP/CFW - SDNAND root"'
	]
}
