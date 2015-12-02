template <class T>
class noncopyable
{
protected:
    noncopyable() {};
    ~noncopyable() {};
private:
    noncopyable(const noncopyable &) = delete;
    noncopyable& operator= (const noncopyable&) = delete;
};