bin_PROGRAMS = enum

enum_LDADD = -lm

enum_SOURCES = \
	assertion.h \
	main.c \
	info.c \
	info.h \
	utils.c \
	utils.h \
	parsing.c \
	parsing.h \
	printing.c \
	printing.h \
	generator.c \
	generator.h

if ! USE_SYSTEM_GETOPT
enum_CPPFLAGS = -I../thirdparty/glibc-2.11.1/posix
enum_SOURCES += \
	../thirdparty/glibc-2.11.1/posix/getopt.h \
	../thirdparty/glibc-2.11.1/posix/getopt.c
endif
