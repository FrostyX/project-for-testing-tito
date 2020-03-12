Name: enum
Version: 1.3
Release: 1%{?dist}
Summary: Seq- and jot-like enumerator

License: BSD
URL:     https://fedorahosted.org/enum
# Sources can be obtained by
# git clone https://github.com/FrostyX/project-for-testing-tito.git
# cd project-for-testing-tito
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

# Source1: somecool.macros
# %%include %{SOURCE1}

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
# %%license %{COPYFILE}
%license COPYING
%doc ChangeLog
%_mandir/man1/enum.1*
# %%{BINARY}
%_bindir/enum


%changelog
* Thu Mar 12 2020 Jakub Kadlcik <frostyx@email.cz> 1.3-1
- disable source1 (frostyx@email.cz)
- foo (frostyx@email.cz)
- Subproject (frostyx@email.cz)

* Wed Mar 11 2020 Jakub Kadlcik <frostyx@email.cz> 1.3-1
- Update source0 (frostyx@email.cz)
- macro for binary (frostyx@email.cz)
- uppercase source1 (frostyx@email.cz)
- use macro in source1 (frostyx@email.cz)
- source1 (frostyx@email.cz)
- change (frostyx@email.cz)

* Fri Dec 20 2019 Jakub Kadlcik <frostyx@email.cz> 1.2-1
- new package built with tito

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
