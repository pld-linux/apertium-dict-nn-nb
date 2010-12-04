Summary:	Norwegian Bokmaal-Nynorsk language pair for Apertium
Summary(pl.UTF-8):	Para języków norweskich bokmaal-nynorsk dla Apertium
%define	lpair	nn-nb
Name:		apertium-dict-%{lpair}
Version:	0.7.0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	708ece31d9017963f2adac14a30fdf62
URL:		http://www.apertium.org/
BuildRequires:	apertium-devel >= 3.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	lttoolbox >= 3.2.0
BuildRequires:	pkgconfig
BuildRequires:	vislcg3 >= 0.9.7.5129
Requires:	apertium >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apertium language pair, which can be used for translating
between Norwegian Bokmaal and Nynorsk, morphological analysis or
part-of-speech tagging of both languages.

It also contains Nynorsk "a-maal" (nn_a) variant (the default, nn, is
e-maal).

%description -l pl.UTF-8
Ten pakiet zawiera parę języków dla Apertium służącą do tłumaczenia
między norweskim bokmaal i nynorsk, a także analizy morfologicznej lub
oznaczania części mowy w obu językach.

Pakiet zawiera także wariant "a-maal" (nn_a) języka nynorsk (domyślnym
- nn - jest e-maal).

%prep
%setup -q -n apertium-%{lpair}-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apertium/modes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/nb-nn.mode
%{_datadir}/apertium/modes/nb-nn-cp.mode
%{_datadir}/apertium/modes/nb-nn_a-cp.mode
%{_datadir}/apertium/modes/nb-nn_a.mode
%{_datadir}/apertium/modes/nn-nb.mode
%{_datadir}/apertium/modes/nn-nn_a.mode
%{_datadir}/apertium/modes/nn_a-nn.mode
