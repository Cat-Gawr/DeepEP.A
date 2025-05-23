
#ifndef NV_MATH_H
#define NV_MATH_H

#include <math.h>

#include <nvVector.h>
#include <nvMatrix.h>
#include <nvQuaternion.h>

#define NV_PI   float(3.1415926535897932384626433832795)

namespace nv
{

    typedef vec2<float> vec2f;
    typedef vec3<float> vec3f;
    typedef vec3<int> vec3i;
    typedef vec3<unsigned int> vec3ui;
    typedef vec4<float> vec4f;
    typedef matrix4<float> matrix4f;
    typedef quaternion<float> quaternionf;


    inline void applyRotation(const quaternionf &r)
    {
        float angle;
        vec3f axis;
        r.get_value(axis, angle);
        glRotatef(angle/3.1415926f * 180.0f, axis[0], axis[1], axis[2]);
    }



};

#endif
