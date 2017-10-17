%global repo_owner  lordadamson
%global repo_name   QuickCD
%global repo_commit 2334173fc227248de0385d2236668bd983022a32

Name:	 quickcd
Version: 20171014
Release: 2%{?dist}
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
# The bashrc adds a "qcd" function.
# Change the path to the main script to an absolute one.
sed -e 's|qcd\.sh|%{_datadir}/qcd/qcd.sh|' -i ./bashrc

%build
# rpmbuild doesn't like it when %%build is missing, so we keep it even though it's empty.

%install
install -m 755 -d %{buildroot}/%{_sysconfdir}/profile.d
install -m 755 -p ./bashrc %{buildroot}/%{_sysconfdir}/profile.d/qcd.sh

install -m 755 -d %{buildroot}/%{_datadir}/qcd 
install -m 755 -p ./qcd.sh %{buildroot}/%{_datadir}/qcd/qcd.sh

%files
%license LICENSE
%{_sysconfdir}/profile.d/qcd.sh
%{_datadir}/qcd/qcd.sh

%changelog
* Tue Oct 17 2017 suve <veg@svgames.pl> 20171014.2
- qcd won't work as a separate script; it has to be called as a shell function. 
  Move the main script from /usr/bin to /usr/share/qcd and add a file
  in /etc/profile.d to set a function for the user shells.

* Sat Oct 14 2017 suve <veg@svgames.pl> 20171014.1
- Initial packaging

