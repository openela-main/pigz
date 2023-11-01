Name:           pigz
Version:        2.4
Release:        4%{?dist}
Summary:        Parallel implementation of gzip

Group:          Applications/File
License:        zlib
URL:            http://www.zlib.net/pigz/
Source0:        http://www.zlib.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		pigz-annocheck-gcc-flags.patch

BuildRequires:  zlib-devel
BuildRequires:  ncompress

%description
pigz, which stands for parallel implementation of gzip,
is a fully functional replacement for gzip that exploits
multiple processors and multiple cores to the hilt when compressing data.

%prep
%autosetup

%build
%set_build_flags
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fpie -pie"


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
* Tue Dec  3 2019 Prarit Bhargava <prarit@redhat.com> - 2.4-4
- Rebuild to kick process (no changes from previous build) [1624161]

* Mon Sep 24 2018 Prarit Bhargava <prarit@redhat.com> - 2.4-3
- Fix annocheck gcc failures [1624161]

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

