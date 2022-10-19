Summary:	Tool to create a timeline of file activity for mounted file systems
Name:		mac-robber
Version:	1.02
Release:	1
Group:		File tools
License:	GPLv2+
URL:		https://sourceforge.net/projects/mac-robber/
Source0:	https://downloads.sourceforge.net/mac-robber/%{name}-%{version}.tar.gz

%description
mac-robber is a digital forensics and incident response tool that can be used
with The Sleuth Kit to create a timeline of file activity for mounted 
file systems.

%files
%doc CHANGES README
%license COPYING
%{_bindir}/mac-robber

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%before_configure
%make_build CC="$CC" GCC_OPT="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 %{name} %{buildroot}%{_bindir}/

