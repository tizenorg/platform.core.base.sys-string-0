Name:       sys-string
Summary:    System string package for multilinugual support 
Version:    1.1
Release:    2
Group:      TO_BE/FILLED_IN
License:    Apache License, Version 2.0
Source0:    %{name}-%{version}.tar.gz
BuildRequires: gettext-tools

%description
System string package for multilinugual support

%prep
%setup -q

%build
/usr/bin/msgfmt -o ar.mo ar.po
/usr/bin/msgfmt -o az.mo az.po
/usr/bin/msgfmt -o bg.mo bg.po
/usr/bin/msgfmt -o ca.mo ca.po
/usr/bin/msgfmt -o cs.mo cs.po
/usr/bin/msgfmt -o da.mo da.po
/usr/bin/msgfmt -o de_DE.mo de_DE.po
/usr/bin/msgfmt -o el_GR.mo el_GR.po
/usr/bin/msgfmt -o en.mo en.po
/usr/bin/msgfmt -o en_PH.mo en_PH.po
/usr/bin/msgfmt -o en_US.mo en_US.po
/usr/bin/msgfmt -o es_ES.mo es_ES.po
/usr/bin/msgfmt -o es_MX.mo es_MX.po
/usr/bin/msgfmt -o et.mo et.po
/usr/bin/msgfmt -o eu.mo eu.po
/usr/bin/msgfmt -o fi.mo fi.po
/usr/bin/msgfmt -o fr_CA.mo fr_CA.po
/usr/bin/msgfmt -o fr_FR.mo fr_FR.po
/usr/bin/msgfmt -o ga.mo ga.po
/usr/bin/msgfmt -o gl.mo gl.po
/usr/bin/msgfmt -o hi.mo hi.po
/usr/bin/msgfmt -o hr.mo hr.po
/usr/bin/msgfmt -o hu.mo hu.po
/usr/bin/msgfmt -o hy.mo hy.po
/usr/bin/msgfmt -o is.mo is.po
/usr/bin/msgfmt -o it_IT.mo it_IT.po
/usr/bin/msgfmt -o ja_JP.mo ja_JP.po
/usr/bin/msgfmt -o ka.mo ka.po
/usr/bin/msgfmt -o kk.mo kk.po
/usr/bin/msgfmt -o ko_KR.mo ko_KR.po
/usr/bin/msgfmt -o lt.mo lt.po
/usr/bin/msgfmt -o lv.mo lv.po
/usr/bin/msgfmt -o mk.mo mk.po
/usr/bin/msgfmt -o nb.mo nb.po
/usr/bin/msgfmt -o nl_NL.mo nl_NL.po
/usr/bin/msgfmt -o pl.mo pl.po
/usr/bin/msgfmt -o pt_BR.mo pt_BR.po
/usr/bin/msgfmt -o pt_PT.mo pt_PT.po
/usr/bin/msgfmt -o ro.mo ro.po
/usr/bin/msgfmt -o ru_RU.mo ru_RU.po
/usr/bin/msgfmt -o sk.mo sk.po
/usr/bin/msgfmt -o sl.mo sl.po
/usr/bin/msgfmt -o sr.mo sr.po
/usr/bin/msgfmt -o sv.mo sv.po
/usr/bin/msgfmt -o tr_TR.mo tr_TR.po
/usr/bin/msgfmt -o uk.mo uk.po
/usr/bin/msgfmt -o uz.mo uz.po
/usr/bin/msgfmt -o zh_CN.mo zh_CN.po
/usr/bin/msgfmt -o zh_HK.mo zh_HK.po
/usr/bin/msgfmt -o zh_SG.mo zh_SG.po
/usr/bin/msgfmt -o zh_TW.mo zh_TW.po

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/locale/ar/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/az/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/bg/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/ca/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/cs/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/da/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/de_DE/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/el_GR/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/en/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/en_PH/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/en_US/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/es_ES/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/es_MX/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/et/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/eu/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/fi/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/fr_CA/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/fr_FR/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/ga/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/gl/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/hi/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/hr/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/hu/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/hy/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/is/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/it_IT/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/ja_JP/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/ka/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/kk/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/ko_KR/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/lt/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/lv/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/mk/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/nb/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/nl_NL/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/pt_BR/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/pt_PT/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/ro/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/ru_RU/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/sk/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/sl/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/sr/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/sv/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/tr_TR/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/uk/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/uz/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/zh_HK/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/zh_SG/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/locale/zh_TW/LC_MESSAGES/

cp ar.mo %{buildroot}%{_datadir}/locale/ar/LC_MESSAGES/sys_string.mo
cp az.mo %{buildroot}%{_datadir}/locale/az/LC_MESSAGES/sys_string.mo
cp bg.mo %{buildroot}%{_datadir}/locale/bg/LC_MESSAGES/sys_string.mo
cp ca.mo %{buildroot}%{_datadir}/locale/ca/LC_MESSAGES/sys_string.mo
cp cs.mo %{buildroot}%{_datadir}/locale/cs/LC_MESSAGES/sys_string.mo
cp da.mo %{buildroot}%{_datadir}/locale/da/LC_MESSAGES/sys_string.mo
cp de_DE.mo %{buildroot}%{_datadir}/locale/de_DE/LC_MESSAGES/sys_string.mo
cp el_GR.mo %{buildroot}%{_datadir}/locale/el_GR/LC_MESSAGES/sys_string.mo
cp en.mo %{buildroot}%{_datadir}/locale/en/LC_MESSAGES/sys_string.mo
cp en_PH.mo %{buildroot}%{_datadir}/locale/en_PH/LC_MESSAGES/sys_string.mo
cp en_US.mo %{buildroot}%{_datadir}/locale/en_US/LC_MESSAGES/sys_string.mo
cp es_ES.mo %{buildroot}%{_datadir}/locale/es_ES/LC_MESSAGES/sys_string.mo
cp es_MX.mo %{buildroot}%{_datadir}/locale/es_MX/LC_MESSAGES/sys_string.mo
cp et.mo %{buildroot}%{_datadir}/locale/et/LC_MESSAGES/sys_string.mo
cp eu.mo %{buildroot}%{_datadir}/locale/eu/LC_MESSAGES/sys_string.mo
cp fi.mo %{buildroot}%{_datadir}/locale/fi/LC_MESSAGES/sys_string.mo
cp fr_CA.mo %{buildroot}%{_datadir}/locale/fr_CA/LC_MESSAGES/sys_string.mo
cp fr_FR.mo %{buildroot}%{_datadir}/locale/fr_FR/LC_MESSAGES/sys_string.mo
cp ga.mo %{buildroot}%{_datadir}/locale/ga/LC_MESSAGES/sys_string.mo
cp gl.mo %{buildroot}%{_datadir}/locale/gl/LC_MESSAGES/sys_string.mo
cp hi.mo %{buildroot}%{_datadir}/locale/hi/LC_MESSAGES/sys_string.mo
cp hr.mo %{buildroot}%{_datadir}/locale/hr/LC_MESSAGES/sys_string.mo
cp hu.mo %{buildroot}%{_datadir}/locale/hu/LC_MESSAGES/sys_string.mo
cp hy.mo %{buildroot}%{_datadir}/locale/hy/LC_MESSAGES/sys_string.mo
cp is.mo %{buildroot}%{_datadir}/locale/is/LC_MESSAGES/sys_string.mo
cp it_IT.mo %{buildroot}%{_datadir}/locale/it_IT/LC_MESSAGES/sys_string.mo
cp ja_JP.mo %{buildroot}%{_datadir}/locale/ja_JP/LC_MESSAGES/sys_string.mo
cp ka.mo %{buildroot}%{_datadir}/locale/ka/LC_MESSAGES/sys_string.mo
cp kk.mo %{buildroot}%{_datadir}/locale/kk/LC_MESSAGES/sys_string.mo
cp ko_KR.mo %{buildroot}%{_datadir}/locale/ko_KR/LC_MESSAGES/sys_string.mo
cp lt.mo %{buildroot}%{_datadir}/locale/lt/LC_MESSAGES/sys_string.mo
cp lv.mo %{buildroot}%{_datadir}/locale/lv/LC_MESSAGES/sys_string.mo
cp mk.mo %{buildroot}%{_datadir}/locale/mk/LC_MESSAGES/sys_string.mo
cp nb.mo %{buildroot}%{_datadir}/locale/nb/LC_MESSAGES/sys_string.mo
cp nl_NL.mo %{buildroot}%{_datadir}/locale/nl_NL/LC_MESSAGES/sys_string.mo
cp pl.mo %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES/sys_string.mo
cp pt_BR.mo %{buildroot}%{_datadir}/locale/pt_BR/LC_MESSAGES/sys_string.mo
cp pt_PT.mo %{buildroot}%{_datadir}/locale/pt_PT/LC_MESSAGES/sys_string.mo
cp ro.mo %{buildroot}%{_datadir}/locale/ro/LC_MESSAGES/sys_string.mo
cp ru_RU.mo %{buildroot}%{_datadir}/locale/ru_RU/LC_MESSAGES/sys_string.mo
cp sk.mo %{buildroot}%{_datadir}/locale/sk/LC_MESSAGES/sys_string.mo
cp sl.mo %{buildroot}%{_datadir}/locale/sl/LC_MESSAGES/sys_string.mo
cp sr.mo %{buildroot}%{_datadir}/locale/sr/LC_MESSAGES/sys_string.mo
cp sv.mo %{buildroot}%{_datadir}/locale/sv/LC_MESSAGES/sys_string.mo
cp tr_TR.mo %{buildroot}%{_datadir}/locale/tr_TR/LC_MESSAGES/sys_string.mo
cp uk.mo %{buildroot}%{_datadir}/locale/uk/LC_MESSAGES/sys_string.mo
cp uz.mo %{buildroot}%{_datadir}/locale/uz/LC_MESSAGES/sys_string.mo
cp zh_CN.mo %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES/sys_string.mo
cp zh_HK.mo %{buildroot}%{_datadir}/locale/zh_HK/LC_MESSAGES/sys_string.mo
cp zh_SG.mo %{buildroot}%{_datadir}/locale/zh_SG/LC_MESSAGES/sys_string.mo
cp zh_TW.mo %{buildroot}%{_datadir}/locale/zh_TW/LC_MESSAGES/sys_string.mo

%files
%defattr(-,root,root,-)
%{_datadir}/locale/*/LC_MESSAGES/*
