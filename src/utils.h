/*
 * enum - seq- and jot-like enumerator
 *
 * Copyright (C) 2010-2012, Jan Hauke Rahm <jhr@debian.org>
 * Copyright (C) 2010-2012, Sebastian Pipping <sping@gentoo.org>
 * All rights reserved.
 *
 * Redistribution  and use in source and binary forms, with or without
 * modification,  are permitted provided that the following conditions
 * are met:
 *
 *     * Redistributions   of  source  code  must  retain  the   above
 *       copyright  notice, this list of conditions and the  following
 *       disclaimer.
 *
 *     * Redistributions  in  binary  form must  reproduce  the  above
 *       copyright  notice, this list of conditions and the  following
 *       disclaimer   in  the  documentation  and/or  other  materials
 *       provided with the distribution.
 *
 *     * Neither  the name of the <ORGANIZATION> nor the names of  its
 *       contributors  may  be  used to endorse  or  promote  products
 *       derived  from  this software without specific  prior  written
 *       permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT  NOT
 * LIMITED  TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND  FITNESS
 * FOR  A  PARTICULAR  PURPOSE ARE DISCLAIMED. IN NO EVENT  SHALL  THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL,    SPECIAL,   EXEMPLARY,   OR   CONSEQUENTIAL   DAMAGES
 * (INCLUDING,  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES;  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 * STRICT  LIABILITY,  OR  TORT (INCLUDING  NEGLIGENCE  OR  OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef UTILS_H
#define UTILS_H 1

#include <sys/types.h>  /* for size_t */


/** Check whether a flag is set.
 *
 * @param[in] bitfield
 * @param[in] flag
 *
 * @return 1 or 0
 *
 * @since 0.3
 */
#define CHECK_FLAG(bitfield, flag)  (((bitfield) & (flag)) == (flag))


/** @name Min/Max macros
 * Macros to find the smaller/larger number.
 *
 * @param[in] a
 * @param[in] b
 *
 * @return a or b respectively, depending on which is smaller
 *
 * @since 0.3
 */

/*@{*/
#define ENUM_MIN(a, b)  (((a) <= (b)) ? (a) : (b))
#define ENUM_MAX(a, b)  (((a) >= (b)) ? (a) : (b))
/*@}*/


/** Enumeration for unescape options.
 *
 * A group of flags to control the algorithm used to unescape
 * escape seqences.
 *
 * @since 1.0
 */
typedef enum _unescape_options {
	GUARD_PERCENT = 1 << 0   /**< convert '\x25' to "%%", not "%" */
} unescape_options;


char * enum_strdup(const char * text);
char * enum_strndup(const char * text, unsigned int length);
int enum_is_nan_float(float value);
size_t unescape(char * text, unescape_options options);

#endif /* UTILS_H */
