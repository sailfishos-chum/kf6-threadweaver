%global  kf_version 6.6.0

Name:		kf6-threadweaver
Version:	6.6.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon for advanced thread management
License:	CC0-1.0 AND LGPL-2.0-or-later
URL:		https://invent.kde.org/frameworks/threadweaver
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:	kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:  qt6-qttools-devel

%description
KDE Frameworks 6 Tier 1 addon for advanced thread management.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6ThreadWeaver.so.*

%files devel
%doc README.md
%license LICENSES/*.txt
%{_kf6_includedir}/ThreadWeaver/
%{_kf6_libdir}/libKF6ThreadWeaver.so
%{_kf6_libdir}/cmake/KF6ThreadWeaver/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
