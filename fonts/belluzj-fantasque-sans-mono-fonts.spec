%global fontname belluzj-fantasque-sans-mono
%global fontconf 64-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        1.8.0
Release:        1%{?dist}
Summary:        Monospaced font with programming ligatures

License:        OFL
URL:            https://github.com/belluzj/fantasque-sans
Source0:        https://github.com/belluzj/fantasque-sans/releases/download/v%{version}/FantasqueSansMono-NoLoopK.tar.gz
Source1:        %{fontconf}
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib

Requires:       fontpackages-filesystem

%description
A programming font, designed with functionality in mind, and with some
wibbly-wobbly handwriting-like fuzziness that makes it unassumingly cool.

Previously known as Cosmic Sans Neue Mono.

%prep
%setup -q -c -n %{fontname}-%{version}
cp -p %{SOURCE1} .

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p TTF/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
    %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
    %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontcconf} \
    %{buildroot}%{_fontconfig_confdir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
    %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf

%license LICENSE.txt
%doc README.md
%{_datadir}/metainfo/%{fontname}.metainfo.xml


%changelog
* Tue Mar 24 2020 blackfalcon <blackfalcon.ru@gmail.com>
- Initial rpm
