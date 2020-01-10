Summary: GNOME developer documentation
Name: gnome-devel-docs
Version: 3.8.1
Release: 2%{?dist}
License: GFDL
Group: System Environment/Libraries
URL: http://library.gnome.org
#VCS: git:git://git.gnome.org/gnome-devel-docs
Source: http://download.gnome.org/sources/gnome-devel-docs/3.8/%{name}-%{version}.tar.xz
BuildArch: noarch
BuildRequires: docbook-utils
BuildRequires: gettext
BuildRequires: itstool

# Logomarks should be removed and replaced with text
# https://bugzilla.redhat.com/show_bug.cgi?id=814220
Patch0: gnome-devel-docs-3.7.90-logos-removal.patch
BuildRequires: automake autoconf
BuildRequires: yelp-tools

%description
This package contains documents which are targeted for GNOME developers.
It contains, e.g., the Human Interface Guidelines, the Integration Guide
and the Platform Overview.

%prep
%setup -q
%patch0 -p1 -b .logos-removal
rm -f platform-demos/media/fedora.png
rm -f platform-demos/media/opensuse.png
rm -f platform-demos/media/ubuntu.png

%build
aclocal  || :
autoheader  || :
automake  || :
autoconf  || :

%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome


%files -f %{name}.lang
%doc README AUTHORS NEWS COPYING

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.1-2
- Mass rebuild 2013-12-27

* Tue May 14 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Richard Hughes <hughsient@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Wed Jul 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Thu Jun 28 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Fri Apr 20 2012 Tomas Bzatek <tbzatek@redhat.com> - 3.4.1-2
- Replace logomarks with plain text (#814220)

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Fri Feb 24 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Mon Feb  6 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.1-1
- Update to 3.3.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.2-1
- Update to 3.0.2

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Wed Apr  6 2011 Christopher Aillon <caillon@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Mon Mar  7 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.91-1
- Update to 2.91.91

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-1
- Update to 2.91.90

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 28 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Mon Apr 26 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.1-1
- Update to 2.30.1

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Mon Feb 22 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.3-1
- Update to 2.29.3

* Wed Feb 10 2010 Bastien Nocera <bnocera@redhat.com> 2.29.2-1
- Update to 2.29.2

* Tue Jan 26 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.1-1
- Update to 2.29.1

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Mon Aug 24 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.1-1
- Update to 2.27.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Thu Sep  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Wed Feb 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.1-1
- Update to 2.21.1

* Wed Oct 24 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-2
- Incorporate package review feedback

* Tue Oct 23 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Initial packaging
