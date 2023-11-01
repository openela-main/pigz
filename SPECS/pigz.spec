Name:           pigz
Version:        2.5
Release:        4%{?dist}
Summary:        Parallel implementation of gzip
License:        zlib
URL:            https://www.zlib.net/pigz/
Source0:        https://www.zlib.net/%{name}/%{name}-%{version}.tar.gz

# [PATCH0] Portability improvements
Patch0:         c9de6c53dcf3eb1071c7999c8accc43ef2b3f458.patch
# [PATCH1] Fix usage of x2nmodp() when compiling for no threads
Patch1:         f310c0868634a1dbacdcdcb2dbce9501a8a87868.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncompress
BuildRequires:  zlib-devel

%description
pigz, which stands for parallel implementation of gzip,
is a fully functional replacement for gzip that exploits
multiple processors and multiple cores to the hilt when
compressing data.

%prep
%autosetup -p1

%build
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
install -p -D pigz $RPM_BUILD_ROOT%{_bindir}/pigz
pushd $RPM_BUILD_ROOT%{_bindir}; ln pigz unpigz; popd
install -p -D pigz.1 -m 0644 $RPM_BUILD_ROOT%{_datadir}/man/man1/pigz.1

%check
make tests CFLAGS="$RPM_OPT_FLAGS"

%files
%doc pigz.pdf README
%{_bindir}/pigz
%{_bindir}/unpigz
%{_datadir}/man/man1/pigz.*

%changelog
* Wed Oct 06 2021 Prarit Bhargava <prarit@redhat.com> - 2.5-4
- Fix annocheck erros [1956998]

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.5-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.5-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Feb 01 2021 Filipe Rosset <rosset.filipe@gmail.com> - 2.5-1
- Update to 2.5 fixes rhbz#1919623

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Adel Gadllah <adel.gadllah@gmail.com> - 2.4-1
- New upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.3.4-1
- Rebuilt for new upstream release 2.3.4, fixes rhbz #1381067

* Sat Dec 03 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.3.3-5
- Spec clean up

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 2.3.3-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Fri Jan 30 2015 Orion Poplawski <orion@cora.nwra.com> - 2.3.3-1
- Update to 2.3.3, fixes CVE-2015-1191 (bug #1181045)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Adel Gadllah <adel.gadllah@gmail.com> - 2.3.1-1
- Update to 2.3.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 31 2012 Ville Skyttä <ville.skytta@iki.fi> - 2.2.5-1
- Update to 2.2.5.
- Hardlink binaries instead of shipping duplicates (#785834).
- Build with $RPM_LD_FLAGS.
- Run test suite during build.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 Adel Gadllah <adel.gadllah@gmail.com> - 2.2.4-1
- New upstream release

* Wed Jan 18 2012 Adel Gadllah <adel.gadllah@gmail.com> - 2.2.3-1
- New upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 26 2010 Adel Gadllah <adel.gadllah@gmail.com> - 2.1.6-1
- New upstream release

* Sat Sep 26 2009 Adel Gadllah <adel.gadllah@gmail.com> - 2.1.5-3
- Preserve timestamps  

* Sat Sep 26 2009 Adel Gadllah <adel.gadllah@gmail.com> - 2.1.5-2
- Fix license tag

* Fri Sep 25 2009 Adel Gadllah <adel.gadllah@gmail.com> - 2.1.5-1
- Initial package

