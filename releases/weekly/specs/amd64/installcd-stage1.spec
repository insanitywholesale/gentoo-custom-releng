subarch: amd64
version_stamp: latest.zfs
target: livecd-stage1
rel_type: default
profile: default/linux/amd64/17.0/no-multilib
snapshot: latest
source_subpath: default/stage3-amd64-latest
portage_confdir: /root/releng/releases/weekly/portage/isos

livecd/use:
	sqlite
	deprecated
	fbcon
	ipv6
	livecd
	loop-aes
	modules
	ncurses
	nptl
	nptlonly
	pam
	readline
	ssl
	static-libs
	unicode
	xml
	-X
	-firmware
	-redistributable

livecd/packages:
	# begin MYSTUFF
	app-admin/ansible
	app-editors/vim
	app-misc/tmux
	app-portage/layman
	dev-vcs/git
	sys-devel/gcc
	sys-process/htop
	# end MYSTUFF
	app-accessibility/brltty
	app-admin/hddtemp
	app-admin/passook
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-editors/mg
	app-editors/nano
	app-editors/vim
	app-misc/screen
	app-portage/mirrorselect
	app-text/wgetpaste
	media-gfx/fbgrab
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/openssh
	net-misc/rdate
	net-misc/rsync
	net-misc/vconfig
	net-proxy/dante
	net-proxy/tsocks
	sys-apps/busybox
	sys-apps/dmidecode
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/netplug
	sys-apps/sdparm
	sys-block/parted
	sys-block/partimage
	sys-devel/bc
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/f2fs-tools
	sys-fs/lsscsi
	sys-fs/ntfs3g
	sys-fs/xfsprogs
	sys-libs/gpm
	sys-power/acpid
	www-client/links
