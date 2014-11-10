Name:       Siepattu

Summary:    Siepattu Ambience
Version:    0.1.0
Release:    1
Group:      System/GUI/Other
License:    WTFPL
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qmake

Requires:   ambienced

%description
This is a template ambience description

%package ts-devel
Summary:   Translation source for template ambience
License:   WTFPL
Group:     System/GUI/Other

%description ts-devel
Translation source for a template ambience

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(-,root,root,-)
%{_datadir}/ambience/Siepattu/Siepattu.ambience
%{_datadir}/ambience/Siepattu/sounds.index
%{_datadir}/ambience/Siepattu/images/*
%{_datadir}/ambience/Siepattu/sounds/*
%{_datadir}/translations/Siepattu_eng_en.qm

%files -n Siepattu-ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/Siepattu.ts
