%global repo_owner  lordadamson
%global repo_name   QuickCD
%global repo_commit 2334173fc227248de0385d2236668bd983022a32

Name:	 quickcd
Version: 20171014
Release: 1%{?dist}
Summary: Bookmarks for your terminal

License: GPLv3
URL:	 https://github.com/%{repo_owner}/%{repo_name}
Source0: %{URL}/archive/%{repo_commit}.tar.gz#/%{repo_name}-%{repo_commit}.tar.gz

BuildArch: noarch
Requires: bash	

%description
qcd allows you to bookmark frequently visited locations and easily cd into them.

%prep
%setup -q -n %{repo_name}-%{repo_commit}

%build
# rpmbuild doesn't like it when %%build is missing, so we keep it even though it's empty.

%install
install -m 755 -d %{buildroot}/%{_bindir}/qcd 
install -m 755 -p ./qcd.sh %{buildroot}/%{_bindir}/qcd

%files
%license LICENSE
%{_bindir}/qcd

%changelog
* Sat Oct 14 2017 suve <veg@svgames.pl> 20171014.1
- Initial packaging

