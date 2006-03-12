Name:           umem
Version:        1.0
Release:        1%{?dist}
Summary:        Port of Solaris's slab allocator.

Group:          System Environment/Libraries
License:        CDDL
URL:            http://sourceforge.net/projects/umem/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# XXX
#BuildRequires:  
#Requires:       

%description
This a port of Solaris's slab allocator, libumem, to Linux.

"A slab allocator is a cache management structure for efficient use
of [...] memory. [...] It is targeted for use of many small pieces
of memory chunks. By managing small memory chunks in the units
called slabs, this mechanism enables lower fragmentation, fast allocation,
and reclaming memory." (Description sourced from Wikipedia.)

%prep
%setup -q


%build
%configure
%{__make}
%{__make} check


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# Remove the libtool files -- we don't want them.
find $RPM_BUILD_ROOT%{_libdir} -name '*.la' | xargs rm -fv

# Remove the symlink to the SONAME. Let ldconfig manage that.
rm -fv $RPM_BUILD_ROOT%{_libdir}/*.so.[0-9]


%clean
rm -rf $RPM_BUILD_ROOT


%pre
/sbin/ldconfig


%post
/sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYRIGHT INSTALL NEWS OPENSOLARIS.LICENSE README TODO
%{_libdir}/*.so.*


%package devel

Summary: Port of Solaris's slab allocator.

Group: Development/Libraries


%description devel

This contains the libraries and header files for using this port
of Solaris's slab allocator, libumem, to Linux.


%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_includedir}/sys/*.h
%{_libdir}/*.so
%{_libdir}/*.a


%changelog
* Sun Mar 12 2006 Richard Dawe <rich@phekda.gotadsl.co.uk> - 1.0-1
- Initial packaging.
