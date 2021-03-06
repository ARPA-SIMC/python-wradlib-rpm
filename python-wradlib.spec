%if 0%{?rhel} == 7
%define python3_vers python36
%else
%define python3_vers python3
%endif

Name:           python-wradlib
Version:        1.7.0
Release:        1%{?dist}
Summary:        weather radar data processing

License:        MIT
URL:            https://github.com/wradlib/wradlib/
Source0:        https://github.com/wradlib/wradlib/archive/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{python3_vers}-devel
BuildRequires:  %{python3_vers}-setuptools
BuildRequires:  %{python3_vers}-semver

%description
The wradlib project has been initiated in order facilitate the use of
weather radar data as well as to provide a common platform for research
on new algorithms. wradlib is an open source library which is well
documented and easy to use.

%package     -n %{python3_vers}-wradlib
Summary:        weather radar data processing
Requires:  %{python3_vers}-numpy
Requires:  %{python3_vers}-scipy
Requires:  %{python3_vers}-matplotlib
Requires:  %{python3_vers}-h5py
Requires:  %{python3_vers}-h5netcdf
Requires:  %{python3_vers}-netcdf4
Requires:  %{python3_vers}-xarray
Requires:  %{python3_vers}-xmltodict
Requires:  %{python3_vers}-gdal

%description -n %{python3_vers}-wradlib
The wradlib project has been initiated in order facilitate the use of
weather radar data as well as to provide a common platform for research
on new algorithms. wradlib is an open source library which is well
documented and easy to use.

%prep
%autosetup -n wradlib-%{version}

%build
%py3_build

%install
%py3_install

%check
# TODO: tests need WRADLIB_DATA env var set (and data)
#%{__python3} setup.py test

%files -n %{python3_vers}-wradlib
%{_bindir}/testrunner
%{python3_sitelib}/*


%changelog
* Thu Jun 18 2020 Daniele Branchini <dbranchini@arpae.it> - 1.7.0-1
- Upstream update

* Wed May  6 2020 Daniele Branchini <dbranchini@arpae.it> - 1.6.2-2
- Added h5netcdf dependency

* Wed May  6 2020 Daniele Branchini <dbranchini@arpae.it> - 1.6.2-1
- Initial package
