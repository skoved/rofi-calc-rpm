Name:           rofi-calc
Version:        2.4.0
Release:        %autorelease
Summary:        Do live calculations in rofi

License: MIT
URL:     https://github.com/svenstaro/rofi-calc
Source0: %{URL}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: qalculate
BuildRequires: meson
BuildRequires: libtool
BuildRequires: cairo-devel
BuildRequires: rofi-devel
BuildRequires: pkgconfig
BuildRequires: gcc
Requires: qalculate

%description
A rofi plugin that uses qalculate's qalc to parse natural language input and provide results.

%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test

%files
%license
%doc


%changelog
%autochangelog

