Name: enum
Version: 1.1
Release: 9%{?dist}
Summary: Seq- and jot-like enumerator

License: BSD
URL:     https://fedorahosted.org/enum
Source0: https://fedorahosted.org/releases/e/n/enum/%{name}-%{version}.tar.bz2

%description
Utility enum enumerates values (numbers) between two values, possibly
further adjusted by a step and/or a count, all given on the command line.
Before printing, values are passed through a formatter. Very fine control
over input interpretation and output is possible.


%prep
%setup -q


%build
%configure --disable-doc-rebuild
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%check
make check

%files
%license COPYING
%doc ChangeLog
%_mandir/man1/enum.1*
%_bindir/enum


%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 10 2012 Ondrej Vasik <ovasik@redhat.com> - 1.1-1
- new upstream release 1.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Ondrej Vasik <ovasik@redhat.com> - 1.0.3-1
- new upstream version 1.0.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 03 2010 Ondrej Vasik <ovasik@redhat.com> - 1.0.2-1
- new upstream version 1.0.2, fixing flaws found in Fedora
  package review(#648517)

* Mon Nov 01 2010 Ondrej Vasik <ovasik@redhat.com> - 1.0.1-1
- initial Fedora packaging
