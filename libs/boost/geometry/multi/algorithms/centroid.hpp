// Boost.Geometry (aka GGL, Generic Geometry Library)
//
// Copyright Barend Gehrels 2007-2009, Geodan, Amsterdam, the Netherlands.
// Copyright Bruno Lalande 2008, 2009
// Use, modification and distribution is subject to the Boost Software License,
// Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef BOOST_GEOMETRY_MULTI_ALGORITHMS_CENTROID_HPP
#define BOOST_GEOMETRY_MULTI_ALGORITHMS_CENTROID_HPP


#include <boost/range.hpp>

#include <boost/geometry/algorithms/centroid.hpp>
#include <boost/geometry/algorithms/num_points.hpp>
#include <boost/geometry/multi/core/point_type.hpp>
#include <boost/geometry/multi/algorithms/detail/multi_sum.hpp>
#include <boost/geometry/multi/algorithms/num_points.hpp>


namespace boost { namespace geometry
{


#ifndef DOXYGEN_NO_DETAIL
namespace detail { namespace centroid
{


/*!
    \brief Building block of a multi-point, to be used as Policy in the
        more generec centroid_multi
*/
template
<
    typename Point,
    typename Strategy
>
struct centroid_multi_point_state
{
    static inline void apply(Point const& point,
            Strategy const& strategy, typename Strategy::state_type& state)
    {
        strategy.apply(point, state);
    }
};



/*!
    \brief Generic implementation which calls a policy to calculate the
        centroid of the total of its single-geometries
    \details The Policy is, in general, the single-version, with state. So
        detail::centroid::centroid_polygon_state is used as a policy for this
        detail::centroid::centroid_multi

*/
template
<
    typename Multi,
    typename Point,
    typename Strategy,
    typename Policy
>
struct centroid_multi
{
    static inline void apply(Multi const& multi, Point& centroid,
            Strategy const& strategy)
    {
        // If there is nothing in any of the ranges, it is not possible
        // to calculate the centroid
        if (geometry::num_points(multi) == 0)
        {
            throw centroid_exception();
        }

        typename Strategy::state_type state;

        for (typename boost::range_iterator<Multi const>::type
                it = boost::begin(multi);
            it != boost::end(multi);
            ++it)
        {
            Policy::apply(*it, strategy, state);
        }
        Strategy::result(state, centroid);
    }
};



}} // namespace detail::centroid
#endif // DOXYGEN_NO_DETAIL



#ifndef DOXYGEN_NO_DISPATCH
namespace dispatch
{

template
<
    typename MultiPolygon,
    typename Point,
    typename Strategy
>
struct centroid<multi_polygon_tag, MultiPolygon, Point,  Strategy>
    : detail::centroid::centroid_multi
        <
            MultiPolygon,
            Point,
            Strategy,
            detail::centroid::centroid_polygon_state
                <
                    typename boost::range_value<MultiPolygon>::type,
                    Strategy
                >
        >
{};


template
<
    typename MultiPoint,
    typename Point,
    typename Strategy
>
struct centroid<multi_point_tag, MultiPoint, Point,  Strategy>
    : detail::centroid::centroid_multi
        <
            MultiPoint,
            Point,
            Strategy,
            detail::centroid::centroid_multi_point_state
                <
                    typename boost::range_value<MultiPoint>::type,
                    Strategy
                >
        >
{};


} // namespace dispatch
#endif


}} // namespace boost::geometry


#endif // BOOST_GEOMETRY_MULTI_ALGORITHMS_CENTROID_HPP

