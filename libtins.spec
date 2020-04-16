#
# spec file for package libtins
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soname  4
Name:           libtins
Version:        4.2
Release:        0.1
Summary:        C++ library for manipulating raw network packets
License:        BSD-2-Clause
Group:          Productivity/Networking/Other
Url:            http://libtins.github.io/
Source0:        https://github.com/mfontanini/libtins/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The library provides a C++ interface for creating tools which
need to send, receive and manipulate specially crafted packets.

%package     -n %{name}%{soname}
Summary:        C++ library for manipulating raw network packets
Group:          System/Libraries

%description -n %{name}%{soname}
The library provides a C++ interface for creating tools which
need to send, receive and manipulate specially crafted packets.

%package        devel
Summary:        Development files for tins
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}
Requires:       libpcap-devel

%description    devel
This package contains header files, and libraries needed to develop
application that use libtins.

%prep
%setup -q

%build
%cmake -DLIBTINS_ENABLE_CXX11=1 -DLIBTINS_BUILD_TESTS=OFF -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%make_build

%install
%make_install

%files -n %{name}%{soname}
%defattr(-,root,root)
%doc CHANGES.md LICENSE README.md THANKS
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/tins
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so
%exclude /usr/lib/cmake/libtins

%changelog
* Fri Jun  9 2017 idonmez@suse.com
- Devel package must depend on libpcap-devel
* Wed Jun  7 2017 jengelh@inai.de
- Ensure neutrality of description.
* Sat May 27 2017 aloisio@gmx.com
- Update to version 3.5 (see CHANGES.md)
- Refreshed libtins-3.2_build.patch as libtins-3.5_build.patch
* Thu May  7 2015 avvissu@yandex.ru
- Initial release
