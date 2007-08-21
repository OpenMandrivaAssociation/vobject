%define name	vobject
%define version	0.4.8
%define release	%mkrel 1

Summary:	Python module for parsing and generating vCard files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	ASL 1.1
Group:		Development/Python
URL:		http://vobject.skyhouseconsulting.com
Source0:	http://vobject.skyhouseconsulting.com/%{name}-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
vobject is intended to be a full featured Python package for parsing
and generating vCard and vCalendar files.

Currently, iCalendar files are supported and well tested. vCard 3.0
files are supported, and all data should be imported, but only a few
components are understood in a sophisticated way.

%package -n python-%{name}

Summary:	Python module for parsing and generating vCard files
Group:		Development/Python
Requires:	python-dateutil
BuildArch:	noarch

%description -n python-%{name}
vobject is intended to be a full featured Python package for parsing
and generating vCard and vCalendar files.

Currently, iCalendar files are supported and well tested. vCard 3.0
files are supported, and all data should be imported, but only a few
components are understood in a sophisticated way.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%post

%postun

%clean
rm -rf %{buildroot}

%files -n python-%{name}
%defattr(-,root,root)
%doc LICENSE.txt README.txt ACKNOWLEDGEMENTS.txt
%{py_puresitedir}/%{name}
%{_bindir}/ics_diff
%{py_puresitedir}/%{name}-%{version}-py%{pyver}.egg-info

