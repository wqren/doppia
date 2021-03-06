// Boost.Geometry (aka GGL, Generic Geometry Library)
//
// Copyright Barend Gehrels 2007-2009, Geodan, Amsterdam, the Netherlands.
// Copyright Bruno Lalande 2008, 2009
// Use, modification and distribution is subject to the Boost Software License,
// Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)


#ifndef BOOST_GEOMETRY_CORE_RING_TYPE_HPP
#define BOOST_GEOMETRY_CORE_RING_TYPE_HPP


#include <boost/mpl/assert.hpp>
#include <boost/mpl/if.hpp>
#include <boost/type_traits/remove_const.hpp>


#include <boost/geometry/core/tag.hpp>
#include <boost/geometry/core/tags.hpp>


namespace boost { namespace geometry
{

namespace traits
{


/*!
\brief Traits class to indicate ring-type  of a polygon's exterior ring/interior rings
\ingroup traits
\par Geometries:
    - polygon
\par Specializations should provide:
    - typedef XXX type ( e.g. linear_ring<P> )
\tparam Geometry geometry
*/
template <typename Geometry>
struct ring_const_type
{
    BOOST_MPL_ASSERT_MSG
        (
            false, NOT_IMPLEMENTED_FOR_THIS_GEOMETRY_TYPE
            , (types<Geometry>)
        );
};

template <typename Geometry>
struct ring_mutable_type
{
    BOOST_MPL_ASSERT_MSG
        (
            false, NOT_IMPLEMENTED_FOR_THIS_GEOMETRY_TYPE
            , (types<Geometry>)
        );
};


} // namespace traits


#ifndef DOXYGEN_NO_DISPATCH
namespace core_dispatch
{

template <typename GeometryTag, typename Geometry>
struct ring_return_type
{};


template <typename LineString>
struct ring_return_type<linestring_tag, LineString>
{
    typedef LineString& type;
};


template <typename Ring>
struct ring_return_type<ring_tag, Ring>
{
    typedef Ring& type;
};


template <typename Polygon>
struct ring_return_type<polygon_tag, Polygon>
{
    typedef typename boost::remove_const<Polygon>::type nc_polygon_type;

    typedef typename mpl::if_
        <
            boost::is_const<Polygon>,
            typename traits::ring_const_type<nc_polygon_type>::type,
            typename traits::ring_mutable_type<nc_polygon_type>::type
        >::type type;
};


template <typename GeometryTag, typename Geometry>
struct ring_type
{};


template <typename Ring>
struct ring_type<ring_tag, Ring>
{
    typedef Ring type;
};


template <typename Polygon>
struct ring_type<polygon_tag, Polygon>
{
    typedef typename boost::remove_reference
        <
            typename ring_return_type<polygon_tag, Polygon>::type
        >::type type;
};





} // namespace core_dispatch
#endif


/*!
\brief Meta-function which defines ring type of (multi)polygon geometry
\details a polygon contains one exterior ring
    and zero or more interior rings (holes).
    This meta function retrieves the type of the rings
\note Exterior ring and interior rings must have the same ring-type.
\ingroup core
*/
template <typename Geometry>
struct ring_type
{
    typedef typename core_dispatch::ring_type
        <
            typename tag<Geometry>::type,
            Geometry
        >::type type;
};


template <typename Geometry>
struct ring_return_type
{
    typedef typename core_dispatch::ring_return_type
        <
            typename tag<Geometry>::type,
            Geometry
        >::type type;
};


}} // namespace boost::geometry


#endif // BOOST_GEOMETRY_CORE_RING_TYPE_HPP
