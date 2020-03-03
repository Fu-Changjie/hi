# SPEC file overview:
# https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/#con_rpm-spec-file-overview
# Fedora packaging guidelines:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/
%define debug_package %{nil}

Name:		helloworld
Version:	1
Release:	0%{?dist}
Summary:	say hi~aaa
License:        AGPL-3.0

Source0:	helloworld-%{version}.tar.xz

BuildRequires:	gcc-c++
Requires:	gcc-c++

%description


%prep
%setup -q -n helloworld-%{version}


%build
# make %{?_smp_mflags}
gcc a.cpp -lstdc++ -o helloworld

%install
mkdir -p %{buildroot}/bin
install -m 755 helloworld %{buildroot}/bin/


%files
/bin/helloworld
%doc
%license



%changelog
* Tue Feb 18 2020 changjie.fu <changjie.fu@cs2c.com.cn> - 1.0
- Say hi to world!
