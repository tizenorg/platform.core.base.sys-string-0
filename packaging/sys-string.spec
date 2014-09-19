%define _LANG_LIST ar az bg ca cs da de_DE el_GR en en_PH en_US es_ES es_MX \\\
                   et eu fi fr_CA fr_FR ga gl hi hr hu hy is it_IT ja_JP ka \\\
                   kk ko_KR lt lv mk nb nl_NL pl pt_BR pt_PT ro ru_RU sk sl \\\
                   sr sv tr_TR uk uz zh_CN zh_HK zh_SG zh_TW

Name:       sys-string
Summary:    System string package for multilinugual support 
Version:    1.1
Release:    0
Group:      System/Logging
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
Source1001: sys-string.manifest
BuildRequires: gettext-tools
BuildArchitectures: noarch

%description
System string package for multilinugual support files

%prep
%setup -q
cp %{SOURCE1001} .

%build
for lang in %{_LANG_LIST}; do
    %{_bindir}/msgfmt -o ${lang}.mo ${lang}.po
done

%install
rm -rf %{buildroot}
for lang in %{_LANG_LIST}; do
    mkdir -p %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/
    cp ${lang}.mo %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/sys_string.mo
done
%find_lang sys_string

%files -f sys_string.lang
%manifest %{name}.manifest
%defattr(-,root,root,-)
