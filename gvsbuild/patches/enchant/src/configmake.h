#ifndef ENCHANT_CONFIGMAKE_H
#define ENCHANT_CONFIGMAKE_H

#ifndef INSTALLPREFIX
#error INSTALLPREFIX must be supplied by the build system
#endif

#define PKGDATADIR INSTALLPREFIX "/share/enchant"
#define PKGLIBDIR INSTALLPREFIX "/lib/enchant"
#define SYSCONFDIR INSTALLPREFIX "/etc"

#endif
