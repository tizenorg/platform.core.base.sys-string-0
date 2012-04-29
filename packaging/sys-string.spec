Name:       sys-string
Summary:    System string package for multilinugual support 
Version:    0.1.15
Release:    0
Group:      TO_BE/FILLED_IN
License:    Apache License, Version 2.0
Source0:    %{name}-%{version}.tar.gz
BuildRequires: gettext-tools

%description
System string package for multilinugual support

%prep
%setup -q

%build
/usr/bin/msgfmt -o en.mo en.po
/usr/bin/msgfmt -o nl_NL.mo nl_NL.po
/usr/bin/msgfmt -o de_DE.mo de_DE.po
/usr/bin/msgfmt -o zh_HK.mo zh_HK.po
/usr/bin/msgfmt -o zh_CN.mo zh_CN.po
/usr/bin/msgfmt -o ru_RU.mo ru_RU.po
/usr/bin/msgfmt -o ko_KR.mo ko_KR.po
/usr/bin/msgfmt -o zh_TW.mo zh_TW.po
/usr/bin/msgfmt -o ja_JP.mo ja_JP.po
/usr/bin/msgfmt -o es_ES.mo es_ES.po
/usr/bin/msgfmt -o el_GR.mo el_GR.po
/usr/bin/msgfmt -o it_IT.mo it_IT.po
/usr/bin/msgfmt -o tr_TR.mo tr_TR.po
/usr/bin/msgfmt -o pt_PT.mo pt_PT.po
/usr/bin/msgfmt -o fr_FR.mo fr_FR.po


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/locale/en/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/nl_NL/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/de_DE/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/zh_HK/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/ru_RU/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/ko_KR/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/zh_TW/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/ja_JP/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/es_ES/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/el_GR/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/it_IT/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/tr_TR/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/pt_PT/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/fr_FR/LC_MESSAGES/

cp en.mo    %{buildroot}%{_datadir}/locale/en/LC_MESSAGES/sys_string.mo
cp nl_NL.mo %{buildroot}%{_datadir}/locale/nl_NL/LC_MESSAGES/sys_string.mo
cp de_DE.mo %{buildroot}%{_datadir}/locale/de_DE/LC_MESSAGES/sys_string.mo
cp zh_HK.mo %{buildroot}%{_datadir}/locale/zh_HK/LC_MESSAGES/sys_string.mo
cp zh_CN.mo %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES/sys_string.mo
cp ru_RU.mo %{buildroot}%{_datadir}/locale/ru_RU/LC_MESSAGES/sys_string.mo
cp ko_KR.mo %{buildroot}%{_datadir}/locale/ko_KR/LC_MESSAGES/sys_string.mo
cp zh_TW.mo %{buildroot}%{_datadir}/locale/zh_TW/LC_MESSAGES/sys_string.mo
cp ja_JP.mo %{buildroot}%{_datadir}/locale/ja_JP/LC_MESSAGES/sys_string.mo
cp es_ES.mo %{buildroot}%{_datadir}/locale/es_ES/LC_MESSAGES/sys_string.mo
cp el_GR.mo %{buildroot}%{_datadir}/locale/el_GR/LC_MESSAGES/sys_string.mo
cp it_IT.mo %{buildroot}%{_datadir}/locale/it_IT/LC_MESSAGES/sys_string.mo
cp tr_TR.mo %{buildroot}%{_datadir}/locale/tr_TR/LC_MESSAGES/sys_string.mo
cp pt_PT.mo %{buildroot}%{_datadir}/locale/pt_PT/LC_MESSAGES/sys_string.mo
cp fr_FR.mo %{buildroot}%{_datadir}/locale/fr_FR/LC_MESSAGES/sys_string.mo

%files
%defattr(-,root,root,-)
%{_datadir}/locale/*/LC_MESSAGES/*
