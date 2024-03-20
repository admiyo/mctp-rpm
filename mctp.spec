Name:           mctp 
Version:        1.1
Release:        1%{?dist}
Summary:        MCTP Userland tools

License:        GPL2 
URL:            https://github.com/CodeConstruct/mctp 
Source:         %{url}/releases/tag/%{version}/%{name}_%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  cmake


%description
%{summary}

%prep
%setup  -q -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%{_bindir}/mctp
