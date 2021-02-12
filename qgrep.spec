
%global _re2_version c33d1680c7e9ab7edea02d7465a8db13e80b558d
%global _re2_url https://github.com/google/re2/

Name:             qgrep
Version:          1.3
Release:          1%{?dist}
Summary:          A fast grep with index database
 
License:          MIT
URL:              https://github.com/ivzhh/%name
Source0:          %{URL}/archive/v%{VERSION}.zip
Source1:          %{_re2_url}/archive/%{_re2_version}.zip
 
BuildRequires:    gcc-c++
BuildRequires:    lz4-devel
BuildRequires:    cmake >= 3.13
BuildRequires:    make

Requires:         lz4
 
%description
The %name is an implementation of grep database, which allows you to perform
grepping (i.e. full-text searches using regular expressions) over a
large set of files. Searches use the database which is a compressed
and indexed copy of the source data, thus they are much faster compared
to vanilla grep -R.

%prep

%setup -q
%setup -q -T -D -a 1

rmdir extern/re2
mv re2-%{_re2_version} extern/re2

%build
%cmake \
    -DWITH_SUBMODULE_LZ4=OFF \
    -DCMAKE_VERBOSE_MAKEFILE=ON \

%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%name

%changelog
* Thu Feb 11 2021 Sheng Mao <shngmao@gmail.com> - 1.3-1
- Initial package
