%if 0%{?rhel} == 7
%define python3_vers python36
%else
%define python3_vers python3
%endif

Name:           python-wradlib
Version:        1.13.0
Release:        1%{?dist}
Summary:        weather radar data processing

License:        MIT
URL:            https://github.com/wradlib/wradlib/
Source0:        https://files.pythonhosted.org/packages/45/99/fa4383be69c7a82ede6f1ef22d215b0efb8c582eec4f5f65ba236eb47524/wradlib-1.13.0.tar.gz
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
%{python3_sitelib}/*


%changelog
* Tue Nov 23 2021 Daniele Branchini <dbranchini@arpae.it> - 1.13.0-1
- Upstream update

* Thu Jun 18 2020 Daniele Branchini <dbranchini@arpae.it> - 1.7.0-1
- Upstream update

* Wed May  6 2020 Daniele Branchini <dbranchini@arpae.it> - 1.6.2-2
- Added h5netcdf dependency

* Wed May  6 2020 Daniele Branchini <dbranchini@arpae.it> - 1.6.2-1
- Initial package
