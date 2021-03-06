subarch: i686
version_stamp: dolphin-2005.0
target: livecd-stage1
rel_type: default
profile: default-linux/x86/2005.0
snapshot: 20050331
source_subpath: default/stage3-i686-2005.0
livecd/use:
	-*
	ipv6
	socks5
	livecd
	fbcon
	minimal
	ncurses
	readline
	samba
	alsa
	ssl
	
livecd/packages:
	baselayout
	livecd-tools
	module-init-tools
	dhcpcd
	udev
	gentoo-sources
	kudzu-knoppix
	hotplug
	coldplug
	fxload
#	tsocks
	irssi
	gpm
	syslog-ng
	parted
	links
	raidtools
	nfs-utils
	jfsutils
	usbutils
	pciutils
	xfsprogs
	e2fsprogs
	reiserfsprogs
	dosfstools
	ext2resize
#	cryptsetup
	pwgen
	popt
	dialog
	rp-pppoe
	screen
	mirrorselect
	penggy
	iputils
	hwdata-knoppix
	hwsetup
	device-mapper
	lvm2
	evms
	vim
	pptpclient
	mdadm
	ethtool
	wireless-tools
	ntfsprogs
	dosfstools
	prism54-firmware
	wpa_supplicant
	genkernel
#	RESCUE_CD
	zsh
	samba
	bacula
	mc
	dar
	mutt
	xfsdump
	ide-smart
	netcat
	nmap
	chkrootkit
#	shfs
	rkhunter
	memdump
	wireless-tools
	x86info
	tar
	bzip2
	gzip
	tct
	partimage	
	ncftp
	rdiff-backup
	rsync
	testdisk
	dd-rescue
	disktype
	centericq
	bind-tools
	alsa-utils
	mpg321
	
